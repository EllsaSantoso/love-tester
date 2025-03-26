document.getElementById('testButton').addEventListener('click', function () {
    const name1 = document.getElementById('name1').value.trim();
    const name2 = document.getElementById('name2').value.trim();

    console.log("Nama 1:", name1, "Nama 2:", name2); // Log nama input

    if (name1 === '' || name2 === '') {
        document.getElementById('result').textContent = 'Please enter both names.';
        return;
    }

    console.log("Mengganti latar belakang..."); // Log saat mengganti latar
    document.body.style.backgroundImage = "url('images/background-game.png')";

    const compatibility = Math.floor(Math.random() * 101);
    console.log("Compatibility:", compatibility); // Log hasil persentase

    document.getElementById('result').innerHTML = `
        ❤️ ${name1} & ${name2} are ${compatibility}% compatible! ❤️
    `;
});
