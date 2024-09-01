const newTaskInput = document.getElementById('newTask');
const newTaskUrgency = document.getElementById('urgency');
const addTaskButton = document.getElementById('addTaskButton');
const taskList = document.getElementById('taskList');

document.addEventListener('DOMContentLoaded', loadTasks);

addTaskButton.addEventListener('click', checkUrgency);

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

function addTask() {
    const taskText = newTaskInput.value.trim();
    const taskUrgency = newTaskUrgency.value;

    if (taskText === '') {
        alert('Por favor, insira uma tarefa.');
        return;
    }

    const li = document.createElement('li');
    li.textContent = taskText + ": " + taskUrgency + " pontos";

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remover';
    removeButton.className = 'remove-button';
    removeButton.addEventListener('click', () => {
        li.remove();
        saveTasks();
    });

    li.appendChild(removeButton);
    li.addEventListener('click', () => {
        li.classList.toggle('completed');
        saveTasks();
    });
    taskList.appendChild(li);
    newTaskInput.value = '';

    updateTasks();
    saveTasks();
}

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

function saveTasks() {
    const tasks = [];
    taskList.querySelectorAll('li').forEach(task => {
        tasks.push({
            text: task.textContent.replace('Remover', '').trim(),
        });
    });
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function loadTasks() {
    const savedTasks = JSON.parse(localStorage.getItem('tasks'));
    if (savedTasks) {
        savedTasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = task.text;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remover';
            removeButton.className = 'remove-button';
            removeButton.addEventListener('click', () => {
                li.remove();
                saveTasks();
            });

            li.appendChild(removeButton);
            taskList.appendChild(li);
        });
    }
}