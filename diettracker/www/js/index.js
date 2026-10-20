document.addEventListener('deviceready', onDeviceReady, false);

if (!window.cordova) {
    window.onload = onDeviceReady;
}

// Stato dell'applicazione
let dailyFoods = [];
const DAILY_GOAL = 2000;

function onDeviceReady() {
    loadData();
    setupEventListeners();
    updateUI();
}

function loadData() {
    const saved = localStorage.getItem('diet_tracker_foods');
    if (saved) {
        try {
            dailyFoods = JSON.parse(saved);
        } catch (e) {
            dailyFoods = [];
        }
    } else {
        dailyFoods = [];
    }
}

function saveData() {
    localStorage.setItem('diet_tracker_foods', JSON.stringify(dailyFoods));
}

function setupEventListeners() {
    const form = document.getElementById('add-food-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const nameInput = document.getElementById('food-name');
        const calInput = document.getElementById('food-calories');

        const name = nameInput.value.trim();
        const cals = parseInt(calInput.value, 10);

        if (name && !isNaN(cals)) {
            addFood(name, cals);
            nameInput.value = '';
            calInput.value = '';
            // Rimuovi il focus (tastiera su mobile si chiude)
            nameInput.blur();
            calInput.blur();
        }
    });

    document.getElementById('btn-clear').addEventListener('click', function() {
        if (confirm('Vuoi azzerare il diario di oggi?')) {
            dailyFoods = [];
            saveData();
            updateUI();
        }
    });
}

function addFood(name, calories) {
    dailyFoods.push({
        id: Date.now(),
        name: name,
        calories: calories
    });
    saveData();
    updateUI();
}

function removeFood(id) {
    dailyFoods = dailyFoods.filter(f => f.id !== id);
    saveData();
    updateUI();
}

function updateUI() {
    const listElement = document.getElementById('food-list');
    listElement.innerHTML = '';

    let totalCals = 0;

    if (dailyFoods.length === 0) {
        listElement.innerHTML = '<li><span class="food-item-name" style="font-weight:normal; color:#999;">Nessun pasto registrato oggi.</span></li>';
    } else {
        dailyFoods.forEach(food => {
            totalCals += food.calories;

            const li = document.createElement('li');

            const nameSpan = document.createElement('span');
            nameSpan.className = 'food-item-name';
            nameSpan.textContent = food.name;

            const rightDiv = document.createElement('div');

            const calSpan = document.createElement('span');
            calSpan.className = 'food-item-cals';
            calSpan.textContent = food.calories + ' kcal';

            const delBtn = document.createElement('button');
            delBtn.className = 'delete-btn';
            delBtn.textContent = '✕';
            delBtn.onclick = function() { removeFood(food.id); };

            rightDiv.appendChild(calSpan);
            rightDiv.appendChild(delBtn);

            li.appendChild(nameSpan);
            li.appendChild(rightDiv);

            listElement.appendChild(li);
        });
    }

    document.getElementById('total-calories').textContent = totalCals;
    updateAdvice(totalCals);
}

function updateAdvice(totalCals) {
    const adviceBox = document.getElementById('advice-box');
    let adviceText = '';

    if (totalCals === 0) {
        adviceText = "Inizia registrando il tuo primo pasto della giornata! Ricorda di bere molta acqua e mangiare frutta e verdura.";
    } else if (totalCals < 500) {
        adviceText = "Hai appena iniziato la giornata. Un pasto ricco di proteine o fibre ti darà l'energia necessaria.";
    } else if (totalCals >= 500 && totalCals < DAILY_GOAL * 0.8) {
        adviceText = "Stai andando bene! Cerca di bilanciare carboidrati e proteine nei prossimi pasti. Un frutto o uno yogurt sono ottimi spuntini.";
    } else if (totalCals >= DAILY_GOAL * 0.8 && totalCals <= DAILY_GOAL * 1.1) {
        adviceText = "Sei vicino al tuo fabbisogno giornaliero raccomandato. Ottimo lavoro per mantenere un apporto equilibrato!";
    } else {
        adviceText = "Attenzione, potresti aver superato il tuo obiettivo calorico giornaliero. Per cena considera un pasto leggero a base di verdure.";
    }

    adviceBox.textContent = adviceText;
}

// Esponi per il testing/console
window.DietApp = {
    getFoods: () => dailyFoods,
    addFood: addFood,
    removeFood: removeFood,
    clear: () => { dailyFoods = []; saveData(); updateUI(); }
};
