<template>
  <div class="faq-view">
    <Header />
    <main class="faq-container">
      <h1>Часто задаваемые вопросы</h1>
      <div v-for="(item, index) in faqItems" :key="index" class="faq-item">
        <div class="faq-question" @click="toggle(index)">
          <p>{{ item.question }}</p>
          <span
            :class="{ 'arrow-down': activeIndex === index, 'arrow-right': activeIndex !== index }"
          >
            {{ activeIndex === index ? '\u25B6' : '\u25B6' }}
          </span>
        </div>
        <div v-if="activeIndex === index" class="faq-answer">
          <p>{{ item.answer }}</p>
        </div>
      </div>
      <div class="button-container">
        <button class="styled-button-1">
          <img src="@/assets/tg-logo.png" alt="Icon" class="button-icon" />
          Задать вопрос
        </button>
        <button class="styled-button-2">
          <img src="@/assets/whatsapp-logo.png" alt="Icon" class="button-icon" />
          Задать вопрос
        </button>
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
      activeIndex: null,
      faqItems: [
        {
          question: 'Я боюсь, что эспандер порвется и ударит меня.',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Можно ли заниматься с эспандерами мужчинам?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Почему эспандеры и ленты ' + '#RAKAMAKAFIT лучше гантелей и штанги?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Как правильно подобрать ' + 'ленту и эспандер для упражнения?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Как заказать RAKAMAKAFIT в Украину?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'У вас экологичное производство?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Возможна ли доставка в другие страны?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question: 'Могу ли я вернуть товар и получить деньги обратно?',
          answer: 'Ответ на этот вопрос...',
        },
        {
          question:
            'Можно ли с помощью лент и эспандеров прокачать пресс, спину, попу и т. д.? Какими упражнениями?',
          answer: 'Ответ на этот вопрос...',
        },
      ],
    };
  },
  methods: {
    toggle(index) {
      this.activeIndex = this.activeIndex === index ? null : index;
    },
  },
};
</script>

<style scoped>
.faq-view {
  background-color: #fff8e7;
  color: #333;
  text-align: center;
  font-family: Inter;
}

.faq-container {
  max-width: 1200px; /* Максимальная ширина контейнера */
  margin: 0 auto; /* Центрирование по горизонтали */
  padding: 20px;
}

.faq-item {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  font-weight: bold;
  font-size: 18px;
}

.faq-question span {
  font-size: 18px;
  transition: transform 0.3s ease;
}

.faq-answer {
  padding-top: 10px;
  color: #333;
}

.arrow-right {
  transform: rotate(0deg);
}

.arrow-down {
  transform: rotate(90deg);
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-top: 20px;
}

.styled-button-1,
.styled-button-2 {
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  font-size: 20px;
  font-family: 'Lato', sans-serif;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: background-color 0.3s ease;
}

.styled-button-1 {
  background-color: #3396ff;
}

.styled-button-2 {
  background-color: #00e600;
}

.styled-button-1:hover {
  background-color: #0056b3;
}

.styled-button-2:hover {
  background-color: #00b300;
}

.button-icon {
  margin-right: 10px;
  width: 40px;
  height: 40px;
}
</style>
