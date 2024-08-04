document.addEventListener("DOMContentLoaded", function() {
    // Function to handle form submissions
    const handleFormSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        try {
            const response = await fetch(event.target.action, {
                method: 'POST',
                body: formData,
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            if (data.redirect) {
                window.location.href = data.redirect;
            } else {
                alert('Form submitted successfully!');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    };

    // Attach event listener to all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', handleFormSubmit);
    });
});
