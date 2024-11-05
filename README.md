<p align="center">
    <a href="https://github.com/HdShare/GameHelperAction">
        <img src="https://socialify.git.ci/HdShare/GameHelperAction/image?description=1&font=Rokkitt&language=1&name=1&owner=1&theme=Auto" alt="socialify"/>
    </a>
</p>

<p align="center">
    <a href="https://github.com/HdShare/GameHelperAction/stargazers">
        <img src="https://img.shields.io/github/stars/HdShare/GameHelperAction?style=flat-square&label=STARS&color=%23dfb317" alt="stars">
    </a>
    <a href="https://github.com/HdShare/GameHelperAction/network/members">
        <img src="https://img.shields.io/github/forks/HdShare/GameHelperAction?style=flat-square&label=FORKS&color=%2397ca00" alt="forks">
    </a>
    <a href="https://github.com/HdShare/GameHelperAction/issues">
        <img src="https://img.shields.io/github/issues/HdShare/GameHelperAction?style=flat-square&label=ISSUES&color=%23007ec6" alt="issues">
    </a>
    <a href="https://github.com/HdShare/GameHelperAction/pulls">
        <img src="https://img.shields.io/github/issues-pr/HdShare/GameHelperAction?style=flat-square&label=PULLS&color=%23fe7d37" alt="pulls">
    </a>
</p>

---

## 访问统计

<p align="center">
    <a href="https://github.com/HdShare/GameHelperAction">
        <img src="http://profile-counter.glitch.me/GameHelperAction/count.svg" alt="count"/>
    </a>
</p>

---

## 使用说明

请按照以下步骤来配置和使用这个项目：

1. **Fork 项目**：点击项目右上角的 "Fork" 按钮，将这个项目复制到你的 GitHub 账户中。
   (⚠️**对于 Fork 的开发者/用户, 请不要滥用GitHub Action, 因为 GitHub 将计算您的分支 GitHub Actions 使用量并归属到上游存储库,
   这可能导致此上游存储库被 GitHub 禁用**)


2. **设置 Secrets**：在你的 GitHub 仓库中，点击 "Settings"（设置），然后在左侧菜单中，点击 "Secrets"（密钥）。点击 "New
   repository secret"（新建仓库密钥），并添加以下密钥：

   ```
    Name: PushPlus
    Desc: 
        消息推送
    Secrets:
        pushplus_token(已废弃)
        serverchan_token
   
    Name: 和平营地
    Desc: 
        福利中心(每日签到 + 每日任务)
    Secrets:
        pg_enable(true)
        pg_appid
        pg_msdkEncodeParam
        pg_openid
        pg_sig
        pg_timestamp
        pg_roleId
        pg_userId
        pg_token
   
    Name: 王者营地
    Desc: 
        我-每日福利
        游戏-工具箱-战令系统(编写中)
        游戏-每日福利-每日任务(计划中)
    Secrets:
        smoba_enable(true)
        smoba_roleId
        smoba_userId
        smoba_token
        smoba_sMSDKUrlParam
        smoba_sOpenId
        smoba_sCampUserId
   ```

3. **启用 GitHub Actions**：在 "Settings"（设置）页面，点击 "Actions"（操作），然后在 "General"（通用）部分，选择 "Read and write
   permissions"（读写权限）。勾选 "Allow GitHub Actions to create and approve pull requests"（允许 GitHub Actions
   创建和批准拉取请求），然后点击 "Save"（保存）。

4. **启用工作流**：在 "Actions"（操作）页面，点击 "I understand my workflows, go ahead and enable them"
   （我了解我的工作流，继续并启用它们），然后点击 "Enable workflow"（启用工作流）。

现在，你的项目应该已经配置好了，并且可以正常运行。

---

## 历史点赞

<p align="center">
    <a href="https://github.com/HdShare/GameHelperAction">
        <img src="https://starchart.cc/HdShare/GameHelperAction.svg?variant=adaptive" alt="starchart">
    </a>
</p>
