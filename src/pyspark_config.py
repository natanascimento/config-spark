import os
import subprocess


class pyspark_config:
    def __init__(self):
        self.BASE_COMMAND = 'pyspark'
        self.BASE_ENV = 'SPARK_PROJECTS'

    def running_spark_project(self):
        os.chdir(os.getenv(self.BASE_ENV))
        subprocess.call(self.BASE_COMMAND, shell=True)


def main():
    main = pyspark_config()
    main.running_spark_project()


if __name__ == '__main__':
    main()
