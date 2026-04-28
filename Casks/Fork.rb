cask "Fork" do
  version "2.63.2"
  sha256 :no_check # 先完成：跳过哈希校验，防止以后更新 DMG 时报错

  # 替换为你实际的 DMG 下载链接
  url "https://cdn.fork.dev/mac/Fork-2.63.2.dmg"
  
  name "Fork"
  desc "Fork is getting better and better day after day and we are happy to share our results with you."
  
  # 这里的名字必须和 DMG 挂载后看到的 .app 名字一模一样
  app "Fork.app" 
end