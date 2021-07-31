from gendiff import generate_diff


answer = u'''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_flat_json():
    a = answer
    b = generate_diff.get_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )

    assert len(a) == len(b)
