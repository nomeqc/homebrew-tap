from pathlib import Path


def main():
    print('tap "nomeqc/tap", trusted: true\n')
    for rb_file in Path(__file__).with_name("Casks").glob("*.rb"):
        print(f'cask "nomeqc/tap/{rb_file.stem}"')


if __name__ == "__main__":
    main()
