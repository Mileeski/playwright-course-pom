def test_005_verificar_pix_acima_limite(page, login_page, home_page, pix_page, common_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("999.999.999-99", "3001")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")