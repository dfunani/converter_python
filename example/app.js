
// Tab switching logic
const tabConverters = document.getElementById('tab-converters');
const tabJson = document.getElementById('tab-json');
const sectionConverters = document.getElementById('section-converters');
const sectionJson = document.getElementById('section-json');

tabConverters.addEventListener('click', () => {
    tabConverters.classList.add('active');
    tabJson.classList.remove('active');
    sectionConverters.style.display = '';
    sectionJson.style.display = 'none';
});

tabJson.addEventListener('click', () => {
    tabJson.classList.add('active');
    tabConverters.classList.remove('active');
    sectionJson.style.display = '';
    sectionConverters.style.display = 'none';
});

// Converter button logic
document.getElementById('convert-btn').addEventListener('click', function() {
    const converter = document.getElementById('converter-select').value;
    const convertTo = document.getElementById('convert-to').value;
    const inputValue = document.getElementById('input-value').value;
    // Conversion logic would go here
    document.getElementById('result').textContent = `Converted value will appear here.`;
});

// JSON Viewer logic
const jsonInput = document.getElementById('json-input');
const jsonOutput = document.getElementById('json-output');
if (jsonInput) {
    jsonInput.addEventListener('input', function() {
        try {
            const parsed = JSON.parse(jsonInput.value);
            jsonOutput.textContent = JSON.stringify(parsed, null, 2);
            jsonOutput.style.color = '#374151';
        } catch (e) {
            jsonOutput.textContent = 'Invalid JSON';
            jsonOutput.style.color = '#ef4444';
        }
    });
}
