### Fase 0 – Verifica accessi

1. **Repository originale (`skylartaylor/gbos-vm`)**: **Accessibile**. Verificato tramite `git ls-remote https://github.com/skylartaylor/gbos-vm.git`.
2. **Repository di destinazione (`Googlebook-Windows`)**: **Non accessibile**. Il repository corrente (`/app`) è configurato con il remote `https://github.com/OpenPlayer-Team/GBos-winport` e risulta vuoto. Tentando di accedere a `https://github.com/OpenPlayer-Team/Googlebook-Windows.git` o varianti ricevo il seguente errore:

`fatal: could not read Username for 'https://github.com': terminal prompts disabled`

Come da istruzioni, mi fermo qui e non procedo per supposizioni.
