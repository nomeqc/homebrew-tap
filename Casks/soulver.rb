cask "soulver" do
  version "4.0.4"
  sha256 :no_check # 跳过哈希校验，防止以后更新 DMG 时报错

  # 替换为你实际的 DMG 下载链接
  url "https://github.com/nomeqc/my-release/releases/download/20260429/Soulver_4.0.4.dmg"
  
  name "Soulver"
  desc "Soulver 是一款自然语言记事本计算器应用。它帮你想清楚问题，把事情算明白。"
  
  # 这里的名字必须和 DMG 挂载后看到的 .app 名字一模一样
  app "Soulver"
end