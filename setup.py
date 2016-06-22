from setuptools import setup

if __name__ == '__main__':
    setup(
        name='channels_shoutbox',
        description='Shoutbox demo of Django Channels',
        install_requires=[
            'django<1.10',
            'django-pipeline',
            'psycopg2',
            'dj-database-url',
            'channels',
        ],
    )

