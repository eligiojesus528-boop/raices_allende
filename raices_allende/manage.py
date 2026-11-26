#!/usr/bin/env python
"""Punto de entrada del proyecto Django (para ejecutar comandos)."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raices_allende.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Lo instalaste? "
            "Ejecuta: pip install django"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
