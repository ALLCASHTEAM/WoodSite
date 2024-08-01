<template>
  <div class="contact-view">
    <Header />
    <main>
      <div class="contact-page">
        <div class="contact-info">
          <h2>Контакты</h2>
          <p>Адрес</p>
          <p>Москва, Вешних Вод, д 14, стр.2</p>
          <p>Email</p>
          <p>contact@gmail.com</p>
          <p>Телефон</p>
          <p>+79182315619</p>
        </div>
        <div class="contact-form">
          <h2>Свяжитесь с нами</h2>
          <form @submit.prevent="submitForm">
            <div>
              <label for="firstName">Имя</label>
              <input type="text" id="firstName" v-model="firstName" required />
            </div>
            <div>
              <label for="lastName">Фамилия</label>
              <input type="text" id="lastName" v-model="lastName" required />
            </div>
            <div>
              <label for="email">Email</label>
              <input type="email" id="email" v-model="email" required />
            </div>
            <div>
              <label for="message">Сообщение</label>
              <textarea id="message" v-model="message" required></textarea>
            </div>
            <button type="submit">Отправить сообщение</button>
          </form>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/header.vue';
import Footer from '@/components/footer.vue';

export default {
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      message: '',
    };
  },
  methods: {
    submitForm() {
      // Логика отправки формы
      alert('Форма отправлена!');
    },
  },
};
</script>

<style scoped>
.contact-page {
  display: flex;
  justify-content: center; /* Центрирование по горизонтали */
  align-items: center; /* Центрирование по вертикали */
  min-height: 66vh; /* Высота 100% экрана */
  background-color: #fff8e7;
  padding: 20px;
}

.contact-info,
.contact-form {
  max-width: 400px; /* Ограничение ширины для обоих блоков */
  margin: 0 20px; /* Отступ между блоками */
}

.contact-info h2,
.contact-form h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.contact-info p {
  margin: 5px 0;
  font-size: 18px;
}

.contact-form form {
  display: flex;
  flex-direction: column;
}

.contact-form form div {
  margin-bottom: 15px;
}

.contact-form label {
  font-size: 16px;
  margin-bottom: 5px;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact-form button {
  padding: 10px 20px;
  background-color: #3396ff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
}

.contact-form button:hover {
  background-color: #0056b3;
}
</style>
