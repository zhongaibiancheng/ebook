# Vue Static Site Template

This template should help get you started developing with a static Vue 3 web application built with Vite and styled with Vuetify.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

### Step 1 - Create new Repo

Create a new project in Github. You can either reference this template repo, or create an empty repository and clone this template repo. To clone, follow this process:

```bash
git clone git@github.com:JoelYoung01/VueStaticSiteTemplate.git <project_name_here>
cd <project_name_here>
git init
git add .
git commit -m "Initial Commit"
git remote add origin <new_repo_url>
git push -u origin main
```

### Step 2 - Setup Environment

Copy `.envtemplate` to a new file, `.env`, and fill out applicable values

### Step 3 - Install Dependencies

Install dependencies

```bash
pnpm i
```

### Run / Build / Deploy

#### Compile and Hot-Reload for Development

```bash
pnpm dev
```

#### Type-Check, Compile and Minify for Production

```bash
pnpm build
```

#### Lint with [ESLint](https://eslint.org/)

```bash
pnpm lint
```
