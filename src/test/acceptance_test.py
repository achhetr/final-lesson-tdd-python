from router import Router

def test_acceptance():
  item = {
    'banana': 1,
    'apple': 1
  }

  assert Router(item).display_receipt() == 'Total value $20'
