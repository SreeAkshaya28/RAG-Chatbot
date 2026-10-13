# RAG Chatbot - Frontend Interface

Next.js interactive user interface for the **RAG Chatbot**, built with **Next.js 16**, **React 19**, and **Tailwind CSS**.

---

## Features

- ⚡ **Real-time Streaming**: Renders incoming LLM response tokens on the fly using ReadableStream and TextDecoder.
- 🎨 **Modern Clean UI**: Responsive card layout with auto-scrolling message feeds and typing indicators.
- 🌓 **Dark Mode Support**: Seamless slate theme styles for light and dark environments.
- ⌨️ **Keyboard Accessibility**: Supports `Enter` to send and `Shift + Enter` for multiline prompts.

---

## Architecture Overview

```
frontend/
├── app/
│   ├── components/
│   │   └── Chat.tsx        # Chat interface with streaming & token deduplication
│   ├── favicon.ico
│   ├── globals.css         # Tailwind & theme styles
│   ├── layout.tsx          # Root layout with Geist font and metadata
│   └── page.tsx            # Main application page
├── public/                 # Static assets
├── next.config.ts          # Next.js configuration
├── package.json            # Project dependencies & scripts
├── tsconfig.json           # TypeScript configuration
└── .env.example            # Environment variables template
```

---

## Getting Started

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Configure Environment (Optional)
Copy `.env.example` to `.env.local` if you need to point to a custom backend host:
```bash
cp .env.example .env.local
```

### 3. Run Development Server
```bash
npm run dev
```

The application will be live at:
[http://localhost:3000](http://localhost:3000)

### 4. Build for Production
```bash
npm run build
npm run start
```

---

## Author

Developed by **M R Sree Akshaya** ([@SreeAkshaya28](https://github.com/SreeAkshaya28)).
