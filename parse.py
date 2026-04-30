import re
from pathlib import Path
from urllib import parse

"""使用说明：
https://github.com/nomeqc/my-release/releases/download/20260429/Alfred_5.7.2.dmg	Alfred_5.7.2.dmg	Alfred

==>

cask "alfred" do
  version "5.7.2"
  sha256 :no_check # 跳过哈希校验，防止以后更新 DMG 时报错

  # 替换为你实际的 DMG 下载链接
  url "https://github.com/nomeqc/my-release/releases/download/20260429/Alfred_5.7.2.dmg"
  
  name "Alfred"
  desc ""
  
  # 这里的名字必须和 DMG 挂载后看到的 .app 名字一模一样
  app "Alfred.app" 
end
"""


def encodeURI(s):
    return parse.quote(s, safe="~@#$&()*!+=:;,.?/'")


def extract_version(text: str):
    version = text.split("_")[-1]
    if bool(re.fullmatch(r"\d+(?:\.\d+)*", version)):
        return version
    return ""


def write_rb_file(app_name_no_ext: str, archive_filename: str, url: str):
    app_name = f"{app_name_no_ext}.app"
    file_name = "".join(app_name_no_ext.lower().split())
    version = extract_version(Path(archive_filename).stem)
    version = version if version else "1.0.0"

    file_parent = Path(__file__).parent
    tpl_content = file_parent.joinpath("template").joinpath("ruby_file.tpl").read_text()
    new_content = (
        tpl_content.replace("{{file_name}}", file_name)
        .replace("{{url}}", url)
        .replace("{{app_name_no_ext}}", app_name_no_ext)
        .replace("{{app_name}}", app_name)
        .replace("{{version}}", version)
    )

    rb_parent = file_parent.joinpath("Casks")
    rb_parent.mkdir(exist_ok=True, parents=True)
    rb_parent.joinpath(f"{file_name}.rb").write_text(new_content)


if __name__ == "__main__":
    input_file = None
    while input_file is None or not Path(input_file).is_file():
        input_text = input("请输入下cask列表文件路径：")
        input_file = Path(input_text)
        if not input_file.is_file():
            print(f"❌找不到文件：{input_file}\n")

    text = input_file.read_text()
    for line in text.splitlines():
        result = re.search(r"(https?://.+?dmg)\s+(.+dmg)\s+(.+)", line.strip())
        if not result:
            continue
        url = encodeURI(result[1])
        archive_filename = result[2]
        app_name = result[3]
        print(url, "\n", app_name)
        write_rb_file(app_name, archive_filename, url)
