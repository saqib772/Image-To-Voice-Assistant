
function translateImage() {
	const imageFile = document.getElementById('image').files[0];
	const language = document.getElementById('language').value;
	const formData = new FormData();
	formData.append('image', imageFile);
	formData.append('language', language);

	fetch('/translate-image', {
		method: 'POST',
		body: formData
	})
	.then(response => response.json())
	.then(data => {
		document.getElementById('result').innerHTML = data.translated_text;
		const audio = new Audio(data.speech_url);
		audio.play();
	});
}
