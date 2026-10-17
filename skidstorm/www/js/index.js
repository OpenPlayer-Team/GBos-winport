document.addEventListener('deviceready', onDeviceReady, false);
// Also start game in browser for testing
if (!window.cordova) {
    window.onload = onDeviceReady;
}

function onDeviceReady() {
    initGame();
}

let canvas, ctx;
let gameLoopId;
let lastTime = 0;

// Game State
const keys = {
    left: false,
    right: false,
    accel: false,
    brake: false
};

const car = {
    x: 0,
    y: 0,
    width: 20,
    height: 40,
    angle: 0,
    speed: 0,
    maxSpeed: 8,
    maxReverseSpeed: -4,
    acceleration: 0.2,
    friction: 0.05,
    brakeForce: 0.3,
    turnSpeed: 0.05,
    driftFactor: 0.9 // Lower = more drift, 1.0 = grip
};

// Track data (simple loop)
const trackPoints = [
    {x: 100, y: 100},
    {x: 700, y: 100},
    {x: 700, y: 400},
    {x: 100, y: 400}
];
const trackWidth = 80;

let camera = { x: 0, y: 0 };

function initGame() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Initial car position
    car.x = trackPoints[0].x;
    car.y = trackPoints[0].y + trackWidth/2;
    car.angle = 0;

    setupControls();

    requestAnimationFrame(gameLoop);
}

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function setupControls() {
    const bindBtn = (id, key) => {
        const btn = document.getElementById(id);
        if(!btn) return;

        btn.addEventListener('touchstart', (e) => {
            e.preventDefault();
            keys[key] = true;
            btn.classList.add('active');
        });
        btn.addEventListener('touchend', (e) => {
            e.preventDefault();
            keys[key] = false;
            btn.classList.remove('active');
        });
        // Mouse fallback for browser testing
        btn.addEventListener('mousedown', (e) => {
            keys[key] = true;
            btn.classList.add('active');
        });
        btn.addEventListener('mouseup', (e) => {
            keys[key] = false;
            btn.classList.remove('active');
        });
        btn.addEventListener('mouseleave', (e) => {
            keys[key] = false;
            btn.classList.remove('active');
        });
    };

    bindBtn('btnLeft', 'left');
    bindBtn('btnRight', 'right');
    bindBtn('btnAccel', 'accel');
    bindBtn('btnBrake', 'brake');

    // Keyboard fallback
    window.addEventListener('keydown', (e) => {
        if(e.key === 'ArrowLeft' || e.key === 'a') keys.left = true;
        if(e.key === 'ArrowRight' || e.key === 'd') keys.right = true;
        if(e.key === 'ArrowUp' || e.key === 'w') keys.accel = true;
        if(e.key === 'ArrowDown' || e.key === 's') keys.brake = true;
    });
    window.addEventListener('keyup', (e) => {
        if(e.key === 'ArrowLeft' || e.key === 'a') keys.left = false;
        if(e.key === 'ArrowRight' || e.key === 'd') keys.right = false;
        if(e.key === 'ArrowUp' || e.key === 'w') keys.accel = false;
        if(e.key === 'ArrowDown' || e.key === 's') keys.brake = false;
    });
}

function update(dt) {
    // Input & Acceleration
    if (keys.accel) {
        car.speed += car.acceleration;
    } else if (keys.brake) {
        car.speed -= car.brakeForce;
    } else {
        // Friction
        if (car.speed > 0) {
            car.speed -= car.friction;
            if (car.speed < 0) car.speed = 0;
        } else if (car.speed < 0) {
            car.speed += car.friction;
            if (car.speed > 0) car.speed = 0;
        }
    }

    // Limit speed
    if (car.speed > car.maxSpeed) car.speed = car.maxSpeed;
    if (car.speed < car.maxReverseSpeed) car.speed = car.maxReverseSpeed;

    // Steering (only turn if moving)
    if (Math.abs(car.speed) > 0.1) {
        const turnDir = car.speed > 0 ? 1 : -1;
        // Increase drift mechanics: sharp turn reduces speed and changes angle
        if (keys.left) {
            car.angle -= car.turnSpeed * turnDir;
            if(keys.brake && car.speed > 0) car.angle -= car.turnSpeed * turnDir * 0.5; // Drift kick
        }
        if (keys.right) {
            car.angle += car.turnSpeed * turnDir;
            if(keys.brake && car.speed > 0) car.angle += car.turnSpeed * turnDir * 0.5; // Drift kick
        }
    }

    // Velocity vectors (simple physics)
    // Forward velocity based on angle
    const forwardX = Math.cos(car.angle) * car.speed;
    const forwardY = Math.sin(car.angle) * car.speed;

    // Drift / Lateral velocity dampening
    // For a real skidstorm feel, we need lateral velocity.
    // Here we use a simple approach: move exactly where pointing,
    // but visual angle might differ if we added complex physics.
    // For now, simple vector movement.

    car.x += forwardX;
    car.y += forwardY;

    // Update Camera
    camera.x = car.x - canvas.width / 2;
    camera.y = car.y - canvas.height / 2;
}

function drawTrack() {
    ctx.save();
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';

    // Draw track surface
    ctx.beginPath();
    ctx.moveTo(trackPoints[0].x, trackPoints[0].y);
    for(let i=1; i<trackPoints.length; i++) {
        ctx.lineTo(trackPoints[i].x, trackPoints[i].y);
    }
    ctx.closePath();

    ctx.lineWidth = trackWidth;
    ctx.strokeStyle = '#555';
    ctx.stroke();

    // Draw center line
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#fff';
    ctx.setLineDash([20, 20]);
    ctx.stroke();

    ctx.restore();
}

function drawCar() {
    ctx.save();
    ctx.translate(car.x, car.y);
    ctx.rotate(car.angle);

    // Car Body
    ctx.fillStyle = '#ff3333';
    ctx.fillRect(-car.height/2, -car.width/2, car.height, car.width);

    // Windshield
    ctx.fillStyle = '#111';
    ctx.fillRect(0, -car.width/2 + 2, 5, car.width - 4);

    // Rear Window
    ctx.fillRect(-car.height/2 + 2, -car.width/2 + 2, 4, car.width - 4);

    ctx.restore();
}

function draw() {
    // Clear screen
    ctx.fillStyle = '#2a802a'; // Grass background
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.save();
    // Apply camera transform
    ctx.translate(-camera.x, -camera.y);

    drawTrack();
    drawCar();

    ctx.restore();
}

function gameLoop(timestamp) {
    if (!lastTime) lastTime = timestamp;
    const dt = timestamp - lastTime;
    lastTime = timestamp;

    update(dt);
    draw();

    gameLoopId = requestAnimationFrame(gameLoop);
}
