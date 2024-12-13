from app.utils.logging import CustomLogger

logger = CustomLogger('volunteer', 'volunteer.log')
logger.info('Volunteer module started')

def run():
    print('Volunteer module is running')


if __name__ == '__main__':
    run()