document.getElementById('markdown-input').addEventListener('input', function() {
    const input = this.value;
    const preview = document.getElementById('preview');
    preview.innerHTML = marked(input);  // Converts markdown to HTML
});
