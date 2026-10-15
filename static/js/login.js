document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

        const user_val = document.getElementById('username').value;
        const pass_val = document.getElementById('password').value;

        const payload = JSON.stringify({
            username: user_val, 
            password: pass_val
        });

        fetch('/api/users/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                },
            body: payload
        })

        .then(response => {
            if (!response.ok) {
                console.log("Response status error:", response.status);
            }
            return response.json();
        })
        .then(data => {
            if (data.token) {
                console.log("Login Success! Token is :", data.token);

                localStorage.setItem('access_token', data.token.access);
                
                window.location.href = "/store/";
            }else{
                console.log("Something wrong!", data)
            }
        })
    .catch(error => console.error('new error:', error));
});