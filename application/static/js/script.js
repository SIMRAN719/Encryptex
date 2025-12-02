async function transform(operation) {
    const inputText = document.getElementById('input-text').value;
    const outputText = document.getElementById('output-text');
    
    if (!inputText.trim()) {
        alert('⚠️ Please enter some text to transform!');
        return;
    }
    
    const data = {
        cipher_type: cipherType,
        text: inputText,
        operation: operation
    };
    
    if (cipherType === 'vigenere') {
        const keyInput = document.getElementById('key-input');
        if (keyInput) {
            const key = keyInput.value;
            if (!key.trim()) {
                alert('⚠️ Please enter a keyword for Vigenère cipher!');
                return;
            }
            data.key = key;
        }
    } else if (cipherType === 'caesar') {
        const shiftInput = document.getElementById('shift-input');
        if (shiftInput) {
            data.shift = parseInt(shiftInput.value) || 3;
        }
    }
    
    try {
        const response = await fetch('/api/transform', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.success) {
            outputText.value = result.result;
            
            console.log('✓ Transformation successful:', operation);
        } else {
            alert('❌ Error: ' + result.error);
            console.error('Transformation error:', result.error);
        }
    } catch (error) {
        alert('❌ An error occurred: ' + error.message);
        console.error('Fetch error:', error);
    }
}

// Allow Ctrl+Enter to trigger encryption
document.addEventListener('DOMContentLoaded', function() {
    const inputText = document.getElementById('input-text');
    if (inputText) {
        inputText.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                transform('encrypt');
            }
        });
    }
    
    // Log when page loads
    console.log('Encryptex loaded - Cipher type:', cipherType);
});