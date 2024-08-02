document.addEventListener('DOMContentLoaded', function() {
    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach(card => {
        card.addEventListener('mouseover', function() {
            this.querySelector('.add-to-cart').textContent = 'В корзину';
        });

        card.addEventListener('mouseout', function() {
            const priceElement = this.querySelector('.product-info p');
            this.querySelector('.add-to-cart').textContent = priceElement.textContent;
        });
    });
});
