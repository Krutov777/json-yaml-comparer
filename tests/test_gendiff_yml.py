from gendiff import generate_diff


answer = u'''{
    constant: yep
  - test: bar
  + test: foo
  - foo: bar
  + bar: foo
}'''


def test_flat_yml():
    a = answer
    b = generate_diff.generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )

    assert len(a) == len(b)
