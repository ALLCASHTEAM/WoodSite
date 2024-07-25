<template>
  <header class="header">
    <div class="logo">
      <img src="@/assets/logo.jpg" alt="Логотип компании" />
      <h1>Мастерская мебели и лестниц</h1>
    </div>
    <div class="flex-container" style="gap: 20px; padding-right: 1%">
      <router-link to="/" class="no-color-link">Главная</router-link>
      <router-link to="/about" class="no-color-link">О нас</router-link>
      <router-link to="/catalog" class="no-color-link">Каталог</router-link>
      <router-link to="/contact" class="no-color-link">Контакты</router-link>
      <span class="icon">👤</span>
      <span class="icon">🛒</span>
    </div>
  </header>
</template>

<style scoped>
.flex-container {
  display: flex;
}
.flex-container > router-link > a {
  margin: 10px;
  padding: 20px;
}
.no-color-link {
  color: inherit;
  text-decoration: none;
}
.header {
  font-family: Inter;
  font-size: large;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fae6da;
}
.logo {
  display: flex;
  align-items: center;
}
.logo img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
  margin-left: 10px;
}
nav {
  flex-grow: 1;
  display: flex;
  justify-content: space-around;
}
</style>
