cask "numi" do
  version "3.32"
  sha256 :no_check # 跳过哈希校验，防止以后更新 DMG 时报错

  # 替换为你实际的 DMG 下载链接
  url "https://github.com/nomeqc/my-release/releases/download/20260429/Numi_3.32.dmg"
  
  name "Numi"
  desc ""
  
  # 这里的名字必须和 DMG 挂载后看到的 .app 名字一模一样
  app "Numi.app"
end