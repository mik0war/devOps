function calculate(operation) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    if (num1 === '' || num2 === '') {
        document.getElementById('result').value = 'Введите оба числа';
        return;
    }

    fetch(`http://localhost:5000${operation}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            num1: parseFloat(num1),
            num2: parseFloat(num2)
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById('result').value = data.error;
        } else {
            document.getElementById('result').value = data.result;
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('result').value = error.error || 'Ошибка сервера';
    });
}