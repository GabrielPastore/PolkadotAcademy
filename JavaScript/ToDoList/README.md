# To-Do List

## Resume

In this changes, a 'Urgency' feature was added as a way to gamefy the day to day chores. This was possible through the use of the select tag in Index.html as well as changes in Styles.css to enhance the visuals. 'Urgency' will be increased by 1 upon adding new tasks to the list. If one task has 10 urgency points (the maximum amount allowed) it becomes impossible to add any other task until the one with max Urgency gets completed.

### Index.html

The changes featured in index.html was the one previously mentioned: the inclusion of the select tag to get the amount of Urgency for the task. The reason select was chosen instead of a input button was to prevent the user from typing letters and breaking the code.

```
<label for="urgency">Pontos de urgência desta tarefa:</label>
        <select name="urgency" id="urgency">
            <option value=2>2</option>
            <option value=3>3</option>
            <option value=4>4</option>
            <option value=5>5</option>
            <option value=6>6</option>
        </select>
        <br><br>
```

### Style.css

New lines added to make the html additions look better and match the visuals of previous elements in the program.

```
label {
    font-size: 13px;
    text-align: left;
    color: #666;
}

select {
    width: 20%;
    padding: 5px;
    margin-top: 5px;
    margin-bottom: 5px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

select:focus {
    border: 2px solid #000;
}
select:hover {
    cursor: pointer;
}
```

### Script.js

Two functions were added to the script file to make the new features viable: 'checkUrgency' and 'updateTasks'. The first is used whenever the user clicks the "Adicionar Tarefa" button. The function will check if there's any task on the list with 10 Urgency points and raise an alert telling them to complete it before adding another one. If there isn't any task with max Urgency, then the function will call the 'addTask' function normally (as it would happen before 'checkUrgency' creation). 

> addTaskButton.addEventListener('click', checkUrgency);

Making 'checkUrgency' be called on ln 8 instead of 'addTask' will allow the verification process to start. The function begins by creating an array with all elements of the li in the HTML to iterate over every task. If the substring '10' is part of the task's name, it will set 'hasMaxUrgency' to true to raise the alert, otherwise, the code will call 'addTask' normally.

```
function checkUrgency() {
    const tasks = Array.from(taskList.querySelectorAll('li'));
    let hasMaxUrgency = false;
    tasks.forEach(task => {
        const textoTarefa = task.textContent.replace('Remover', '').trim();
        if (textoTarefa.includes('10')) {
            hasMaxUrgency = true;
        }
    });

    if (hasMaxUrgency) {
        alert('Tarefa de urgência máxima detectada. Complete-na antes de adicionar outras.');
    } else {
        addTask();
    }
}
```

The second function, 'updateTasks' is called on ln 55 before saving the list on local storage.

> updateTasks();

The function starts by creating an array of all the tasks presents in the HTML, just like 'checkUrgency' then the function will check if it has more than 1 task to prevent it from raising the Urgency of the first task added as soon as the button is pressed the first time. On every iteration, the loop will use a Regular Expression to search for the first number in the string, if found it will convert it to an Integer to be modified. The number found will be replaced on the string by its successor and the new string will be assigned to task.textContent.

```
function updateTasks() {
    const tasks = Array.from(taskList.querySelectorAll('li'));
    if (tasks.length > 1) {
        tasks.slice(0, -1).forEach(task => {
            const removeButton = task.querySelector('.remove-button');
            let textoTarefa = task.textContent.replace('Remover', '').trim();
            let pontos = parseInt(textoTarefa.match(/\d+/)[0]);

            if (pontos < 10) {
                pontos ++;
                textoTarefa = textoTarefa.replace(/\d+/, pontos);
            }

            task.textContent = textoTarefa;
            task.appendChild(removeButton);
        });
    }
}
```

### Problems to solve

Since the way 'updateTasks' works is by finding the first number in the string, the function will modify the task name sent by the user if the input has any numbers inside it. This issue hasn't been solved yet.