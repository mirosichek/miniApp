let tg = window.Telegram.WebApp;

// Получаем и декодируем initData
let initData = tg.initData || '';
let initDataUnsafe = tg.initDataUnsafe || {};

// Проверяем авторизацию пользователя
if (initDataUnsafe.user) {
    console.log("User is authorized:", initDataUnsafe.user.first_name);
} else {
    console.log("User is not authorized");
}

// Отправляем данные обратно боту
document.getElementById('sendData').addEventListener('click', function() {
    tg.sendData("Some data from Mini App");
});