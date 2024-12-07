document.addEventListener('DOMContentLoaded', () => {
    const addRowBtn = document.getElementById('add-row');
    const tableBody = document.querySelector('#propriedades-tabela tbody');
    const tipos = JSON.parse(document.getElementById('tipos-data').textContent);

    const createRow = () => {
        const newRow = document.createElement('tr');
        let tiposOptions = `<option value="">Selecione um tipo</option>`;
        tipos.forEach(tipo => {
            tiposOptions += `<option value="${tipo.id}">${tipo.NOME}</option>`;
        });

        newRow.innerHTML = `
            <td>
                <select name="tipo_id" class="form-select">
                    ${tiposOptions}
                </select>
            </td>
            <td>
                <input type="number" name="porta" class="form-control">
            </td>
            <td>
                <input type="text" name="descricao" class="form-control">
            </td>
            <td>
                <input type="checkbox" name="remover" class="checkbox">            
            </td>
        `;
        return newRow;
    };

    addRowBtn.addEventListener('click', () => {
        const newRow = createRow();
        tableBody.appendChild(newRow);
    });

    tableBody.addEventListener('click', (e) => {
        if (e.target && e.target.classList.contains('remove-row')) {
            e.target.closest('tr').remove();
        }
    });

    // Preenchimento dos selects para as linhas já existentes
    const selects = document.querySelectorAll('select[name="tipo_id"]');
    selects.forEach(select => {
        const selectedValue = select.getAttribute('data-selected');
        if (selectedValue) {
            select.value = selectedValue;
        }
    });
});
