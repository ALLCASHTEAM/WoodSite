<template>
  <header class="header">
    <div class="logo">
      <img src="@/assets/logo.jpg" alt="Логотип компании" />
      <h1>Мастерская мебели и лестниц</h1>
    </div>
    <nav>
      <router-link to="/">Главная</router-link>
      <router-link to="/about">О нас</router-link>
      <router-link to="/catalog">Каталог</router-link>
      <router-link to="/contact">Контакты</router-link>
    </nav>
    <div class="icons">
      <span class="icon">👤</span>
      <span class="icon">🛒</span>
    </div>
  </header>
</template>

<style scoped>
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
}
nav {
  flex-grow: 1;
  display: flex;
  justify-content: space-around;
}
.icons {
  display: flex;
}
.icon {
  margin-left: 20px;
  cursor: pointer;
}
</style>
