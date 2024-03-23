document.addEventListener("DOMContentLoaded", function() {
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    let month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    let day = currentDate.getDate().toString().padStart(2, '0');
    const minDate = `${year}-${month}-${day}`;
    document.getElementById('due_date').setAttribute('min', minDate);
});