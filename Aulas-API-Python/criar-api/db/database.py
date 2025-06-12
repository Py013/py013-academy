DB: dict[str, dict] = {
    '1': {
        'id': '1',
        'description': 'Notebook Dell Inspiron 15 3000',
        'category': 'Computador',
        'quantity': 450,
        'send_type': 'Nacional',
        'price': 50.70,
    },
   '2': {
        'id': '2',
        'description': 'Placa de vídeo NVIDIA 5090',
        'category': 'Componente eletrônico',
        'quantity': 41,
        'send_type': 'Internacional',
        'price': 68.12,
    },
    '3': {
        'id': '3',
        'description': 'Cadeira gamer com suspensão a ar',
        'category': 'Mobília',
        'quantity': 220,
        'send_type': 'Nacional',
        'price': 335.53,
    },
    '4': {
        'id': '4',
        'description': 'Mouse profissional para designers 3D',
        'category': 'Periferico',
        'quantity': 21,
        'send_type': 'Internacional',
        'price': 225.50,
    },
}


if __name__ == '__main__':
    print(DB)