# base

## Project setup

```
# yarn
yarn

# npm
npm install

# pnpm
pnpm install

# pnpm
bun install
```

### Compiles and hot-reloads for development

```
# yarn
yarn dev

# npm
npm run dev

# pnpm
pnpm dev

# bun
bun run dev
```

### Compiles and minifies for production

```
# yarn
yarn build

# npm
npm run build

# pnpm
pnpm build

# bun
bun run build
```

### Lints and fixes files

```
# yarn
yarn lint

# npm
npm run lint

# pnpm
pnpm lint

# bun
bun run lint
```

### Customize configuration

See [Configuration Reference](https://vitejs.dev/config/).

### 文件架构

1. 配置：当前文件夹下各文件，除了引入新配置一般不用修改
2. src/ 下非目录文件也一般不用修改
3. src/views/ 为各页面的 js 文件
4. src/utils/ 为向后端发起 http 请求时的工具
5. src/styles/ 可以不用管
6. src/store/ 提供在前端存储数据的操作，如存储 token 则用户无需重复登录，可以记忆登录状态
7. src/router/ 提供路由与页面的对应关系
8. src/plugins/ 注册插件，如当前使用的 UI 组件库 Vuetify
9. src/layouts/ 是 vite 搭建框架以后的默认页面，可以不用管，作为参考
10. src/assets/ 放置使用的图片

### 开发提示

如果在开发时想看其他已登录才可查看的页面预览，可以修改 src/router/index.js ，注释部分代码，即可成功进入 URL 对应页面
