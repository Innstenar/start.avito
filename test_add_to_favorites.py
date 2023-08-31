from playwright.sync_api import sync_playwright

def test_add_to_favorites():
    # URL объявления на Avito
    advertisement_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"

    with sync_playwright() as p:
        browser = p.chromium.launch()  # Запуск браузера Chromium
        page = browser.new_page()  # Создание новой страницы

        page.goto(advertisement_url)  # Переход на страницу объявления
        
        # Получение названия товара
        item_name = page.locator("span.title-info-title-text").inner_text()

        # Нажатие на кнопку "Добавить в избранное"
        add_to_favorite_button = page.locator("div.style-header-add-favorite-M7nA2>button.desktop-usq1f1")
        add_to_favorite_button.click()

        # Ожидание, пока кнопка станет в состоянии "Добавлено в избранное"
        page.wait_for_selector("div[class=style-header-add-favorite-M7nA2]>button[data-is-favorite=true]")

        # Переход в список избранное
        go_to_favorites_button = page.locator("div.desktop-1rdftp2")
        go_to_favorites_button.click()

        # Ожидание загрузки страницы избранных и проверка наличия добавленного товара
        page.wait_for_selector(".styles-module-root-hwVld")
        assert item_name in page.content(), "Товар не добавился в избранное"
        print("Объявление успешно добавлено в избранное")

# Запуск теста
if __name__ == "__main__":
    test_add_to_favorites()
