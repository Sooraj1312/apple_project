document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const user_val = document.getElementById('reg_username').value;
    const pass_val = document.getElementById('reg_password').value;

    // എപിഐ-ലേക്ക് അയക്കാനുള്ള ഡാറ്റ 
    const payload = JSON.stringify({
        username: user_val, 
        password: pass_val
    });

    // ഇവിടെ നിന്റെ രജിസ്റ്റർ എപിഐ ലിങ്ക് കൃത്യമായി കൊടുക്കുക (urls.py-ൽ ഉള്ളത് പോലെ)
    fetch('/api/users/register/', {
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
        // രജിസ്ട്രേഷൻ കഴിഞ്ഞാൽ ഉടനെ ടോക്കൺ വരുന്നുണ്ടോ എന്ന് നോക്കുന്നു
        if (data.token) {
            console.log("Register Success! Token is :", data.token);

            // ടോക്കൺ ബ്രൗസറിൽ സേവ് ചെയ്യുന്നു (ലോഗിൻ ചെയ്തത് പോലെ)
            localStorage.setItem('access_token', data.token.access);
            
            // നേരെ സ്റ്റോർ പേജിലേക്ക് പോകുന്നു
            window.location.href = "/store/";
        } else {
            console.log("Something wrong!", data);
            alert("രജിസ്ട്രേഷൻ പരാജയപ്പെട്ടു! ദയവായി വിവരങ്ങൾ പരിശോധിക്കുക.");
        }
    })
    .catch(error => console.error('Error:', error));
});