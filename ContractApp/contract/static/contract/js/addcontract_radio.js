            const types = ['Заказчик', 'Подрядчик'];
            // generate the radio groups
            const group = document.querySelector("#group");
            group.innerHTML = types.map((type) => `<div>
                <input type="radio" name="type" value="${type}" id="${type}">
                 <label for="${type}">${type}</label>
            </div>`).join(' ');
            // add an event listener for the change event
            const radioButtons = document.querySelectorAll('input[name="type"]');
            for (const radioButton of radioButtons) {
                radioButton.addEventListener('change', showSelected);
            }

            function showSelected(e) {
                console.log(e);
                if (this.checked) {
                    kontr_do = document.getElementById('id_do');
                    kontr_do.name = 'kontr'
                    kontr = document.getElementsByName('kontr');

                    kontr_po = document.getElementById('id_po');

                    org = `{{ org }}`;

                    if (this.value == 'Подрядчик') {
                        kontr_po.value = org;
                    }
                    if (this.value == 'Заказчик') {
                        ttt[0].value = org;
                        ttt[0].id = `id_do`;
                        kontr[0].id = 'id_po';
                    }
                }
            }
