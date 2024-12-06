from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Paso 2
    page.goto("https://club-administration.qa.qubika.com/#/auth/login")

    # Paso 3: Validar la página de inicio de sesión
    assert page.locator("text=Qubika Club").is_visible(), "La página de inicio de sesión no se muestra correctamente"

    # Paso 4: Iniciar sesión
    text_input = page.locator('[type="email"]')
    text_input.fill('string')
    pass_input = page.locator('[type="password"]')
    pass_input.fill('string')
    page.click('button[type="submit"]')
    page.wait_for_timeout(1000)

    # Paso 5
    # Validar que se ha iniciado sesión correctamente
    assert "dashboard" in page.url, "No inició sesión correctamente"

    # Paso 6.A
    # Ir a Categoría
    page.click("text= Tipos de Categorias ")
    assert "category-type" in page.url, "No se redirigió a la página de Categorías"

    # Paso 6.B
    # Crear una nueva categoría
    page.click("text=Adicionar")
    page.fill("#input-username", "Nueva Category de Juan")
    page.click('button[type="submit"]')
    page.click("text=133")
    # assert page.locator("text=Nueva Category de Juan").is_visible(), "La categoría no se creó correctamente"

    # Paso 6.C
    # Crear subcategoría
    page.click("text=Adicionar")
    page.fill("#input-username", "Nueva Subcategory")

    # Seleccionar Checkbox de Subcategoría
    # checkbox = page.locator('input[type="checkbox"]')
    # checkbox.check()

    # Seleccionar la categoría que se ha creado anteriormente
    # page.select_option('select[name="option"]', value='Nueva Category de Juan')
    # page.click('button[type="submit"]')
    # assert page.locator("text=Nueva Subcategory de Juan").is_visible(), "La subcategoría no se creó correctamente"

    page.wait_for_timeout(1000)

    page.screenshot(path="demo.png")
    browser.close()