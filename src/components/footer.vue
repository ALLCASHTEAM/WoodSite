<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-info">
        <p>Контакты</p>
        <p>Адрес<br />Москва, Вешних Вод, д 14, стр.2</p>
        <p>Email<br />contact@gmail.com</p>
        <p>Телефон<br />+79182315619</p>
      </div>
      <div class="footer-catalog">
        <p>Столешницы</p>
        <p>Стулья</p>
        <p>Шкафы</p>
        <p>Кресла</p>
      </div>
      <div class="footer-catalog">
        <p>Принадлежности</p>
        <p>Скамейки</p>
        <p>Кровати</p>
        <p>Декор</p>
      </div>
      <div class="footer-brand">
        <img src="@/assets/logo.jpg" alt="Logo Image" class="logo-image" />
        <div>
          <h2>WOODSHOP</h2>
          <p>Пользовательское соглашение</p>
        </div>
        <div class="footer-images">
          <img src="@/assets/tg-logo.png" alt="Telegram" />
          <img src="@/assets/vk-logo.png" alt="Vkontakte" />
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'footer',
};
</script>

<style scoped>
.footer {
  background-color: #5c4d46;
  color: #ffffff;
  padding: 5px 500px;
  font-family: Inter;
}

.footer-content {
  display: flex;
  justify-content: center; /* Выравнивание по центру горизонтально */
}

.footer-catalog {
  line-height: 1.5;
  text-align: left;
  margin-right: 30px;
}

.footer-info {
  line-height: 1.5;
  text-align: left;
  border-right: 1px solid;
  padding-right: 10px;
  margin-right: 15px;
}

.footer-images {
  gap: 10%;
}

.footer-images img {
  width: 30px;
  height: 30px;
  margin-left: 10px;
}

.footer-brand {
  text-align: right;
  line-height: 1.5;
  border-left: 1px solid;
  margin-left: 15px;
  padding-left: 10px;
}

.footer-brand .logo-image {
  width: 60px;
  height: 60px;
  margin-right: 10px;
}

.footer-brand h2 {
  margin: 0;
  font-size: 30px;
  font-weight: bold;
}

.footer-brand p {
  margin: 0;
  font-size: 16px;
}
</style>
