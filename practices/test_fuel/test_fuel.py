import pytest
from practices.test_fuel import convert, gauge


# تست تبدیل ورودی به درصد
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99

    # تست ورودی اشتباه
    with pytest.raises(ValueError):
        convert("10/3")

    with pytest.raises(ZeroDivisionError):
        convert("100/0")

    with pytest.raises(ValueError):
        convert("3/four")

    with pytest.raises(ValueError):
        convert("1.5/4")

    with pytest.raises(ValueError):
        convert("3/5.5")

    with pytest.raises(ValueError):
        convert("5-10")


# تست گاج (خروجی F, E یا درصد)
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


# تست ورودی و اجرای صحیح در main()
@pytest.mark.parametrize("user_input, expected_output", [
    ("3/4", "75%"),
    ("1/3", "33%"),
    ("2/3", "67%"),
    ("0/100", "E"),
    ("1/100", "E"),
    ("100/100", "F"),
    ("99/100", "F"),
])
def test_main(user_input, expected_output, monkeypatch):
    # جایگزینی input با ورودی دلخواه
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    # جایگزینی print برای بررسی خروجی
    monkeypatch.setattr("builtins.print", lambda x: x)

    # اجرای کد اصلی
    result = main()
    assert result == expected_output
