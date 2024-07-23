document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const query = document.getElementById('query').value;

    fetch('http://localhost:5000/submit-query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                phone: phone,
                email: email,
                query: query
            }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Query submitted successfully');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});