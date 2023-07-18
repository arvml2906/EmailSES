/*==============================Submit form============================================*/
function submitForm() {
    // Get form values
    var name = document.querySelector('input[name="name"]').value;
    var email = document.querySelector('input[name="email"]').value;
    var project = document.querySelector('input[name="project"]').value;
    var message = document.querySelector('textarea[name="message"]').value;

    // Create JSON payload
    var payload = JSON.stringify({
        "name": name,
        "email": email,
        "project": project,
        "message": message
    });

    // Make API request
    fetch(' https://xxxxxxxxxxxxx(edit API GATEWAY URL).amazonaws.com/Test/sendmail', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            //'X-Api-Key': 'DB1J2jMhl63org8tZGzwO3uPWOiukScJ4Xr0FX2j'
        },
        body: payload
    })
    .then(function(response) {
        if (response.ok) {
            alert('Message sent successfully!');
        } else {
            alert('Error sending message. Please try again.');
        }
    })
    .catch(function(error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
}