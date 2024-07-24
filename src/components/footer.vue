<template>
  <footer class="footer">
    <div class="footer-content">
      <img src="@/assets/logo.jpg" alt="Логотип компании" />
      <div>
        <p>Адрес: Москва, Вешняковская, д 14, стр.2</p>
        <p>Доставка по всей России</p>
        <p>Телефон: +7 (968) 598-18-04</p>
        <p>Email: master@hardmassive.ru</p>
      </div>
    </div>
    <p>Политика конфиденциальности</p>
    <p></p>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
}
.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.footer-content img {
  width: 50px;
  height: 50px;
}
.footer-content div {
  text-align: left;
}
</style>
