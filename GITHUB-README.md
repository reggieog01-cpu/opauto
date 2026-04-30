# OP Auto Clicker

> The fastest free auto clicker for Windows. 100+ CPS, 1ms minimum interval, F6 hotkey, fixed-position clicking. Open source. 512 KB. No installation, no ads, no bundleware.

🌐 **Website**: [opauto.app](https://opauto.app)
📥 **Download**: [opauto.app/download](https://opauto.app/download)
❓ **FAQ**: [opauto.app/faq](https://opauto.app/faq)
💬 **Issues / Support**: [GitHub Issues](https://github.com/op-auto-clicker/op-auto-clicker/issues)

---

## What is OP Auto Clicker?

OP Auto Clicker is a free, open-source auto clicker for Windows that automates mouse clicks at custom intervals. It's used by Minecraft and Roblox players, software testers, and accessibility users worldwide.

Unlike most free auto clickers, OP Auto Clicker:

- **Sustains 100+ CPS** without dropping clicks (most free options cap at 30–50 CPS)
- **1ms minimum interval** (most cap at 10ms)
- **Portable** — single 512 KB `.exe`, no installer, no admin rights, no registry writes
- **No bundleware** — the binary contains nothing but the auto clicker. No third-party offers, no telemetry, no internet calls
- **Open source** — full source code in this repo, every release signed and scanned by VirusTotal
- **Works on every Windows version** — Windows 7 SP1, 8, 10, 11 (32-bit and 64-bit)

📖 **Full docs and use-case guides**: [opauto.app](https://opauto.app)

---

## Features

| Feature | Details |
|---------|---------|
| Click interval | 1ms to multiple hours, configurable in ms / s / min / hr |
| Click types | Left, right, middle mouse button |
| Click modes | Single, double |
| Click position | Cursor (dynamic) or fixed (X, Y) coordinate |
| Hotkey | F6 default, fully remappable to any key |
| Click count | Unlimited, or stop after N clicks |
| Background operation | Runs from system tray |
| Footprint | 512 KB binary, ~5 MB RAM idle |

---

## Quick Start

1. **Download** the latest `.exe` from [opauto.app/download](https://opauto.app/download) or the [Releases](../../releases) page
2. **Double-click** the file to launch (no installer)
3. Set your **click interval**, **mouse button**, and **hotkey**
4. Press **F6** to start clicking. Press **F6** again to stop

That's it. Full setup walkthrough with screenshots: [opauto.app/how-to-use-auto-clicker](https://opauto.app/how-to-use-auto-clicker)

---

## Common Use Cases

| Use case | Recommended setup | Guide |
|----------|-------------------|-------|
| **Minecraft** mining, fishing, breeding, PvP | 4–15 CPS depending on action | [opauto.app/minecraft-auto-clicker](https://opauto.app/minecraft-auto-clicker) |
| **Roblox** clicker simulators, idle, pet hatching | 20–50 CPS, fixed-position | [opauto.app/roblox-auto-clicker](https://opauto.app/roblox-auto-clicker) |
| **Cookie Clicker** / idle browser games | 15–30 CPS, fixed on cookie | [opauto.app/auto-clicker-for-games](https://opauto.app/auto-clicker-for-games) |
| **Software / UI testing** | 1–5 CPS, scriptable via hotkey | [opauto.app/how-to-use-auto-clicker](https://opauto.app/how-to-use-auto-clicker) |
| **Accessibility** (RSI, limited mobility) | Custom interval, custom hotkey | — |

---

## Why is OP Auto Clicker faster than other auto clickers?

Most free Windows auto clickers cap around 30–50 CPS because of how they handle input:

- **.NET timers** with garbage-collection pauses
- **60Hz frame-locked event loops**
- **Polling-based abstraction layers**

OP Auto Clicker uses a tight native input loop calling Windows' [`SendInput`](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput) directly with [`QueryPerformanceCounter`](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) timing. The result:

| Metric | OP Auto Clicker | Typical free auto clicker |
|--------|----------------:|--------------------------:|
| Sustained CPS at 1ms interval | ~840 CPS | 30–50 CPS |
| Sustained CPS at 10ms interval | 100 CPS exact | 30–50 CPS |
| Timing drift over 60s burst | <1% | 5–15% |
| F6 to first click (warm) | 8 ms | 100–300 ms |
| RAM idle | 4.8 MB | 30–80 MB |

Full benchmark methodology: [opauto.app/fastest-auto-clicker](https://opauto.app/fastest-auto-clicker)

---

## Is OP Auto Clicker safe?

Yes:

- **Open source** — every line of code is public in this repo. Audit it, build it yourself, fork it
- **Code-signed** — every release `.exe` is digitally signed
- **VirusTotal verified** — scanned by 70+ AV engines on every release, zero detections
- **No telemetry** — the binary contains zero networking code. No analytics, no phone-home, no auto-update calls
- **No bundleware** — the `.exe` is the entire app. No installer, no third-party offers
- **SHA256 hash published** — verify your download matches before running

Full safety analysis and how to verify: [opauto.app/safe-auto-clicker](https://opauto.app/safe-auto-clicker)

---

## System Requirements

**Minimum**: Windows 7 SP1, 1 GHz x86/x64 CPU, 256 MB RAM, .NET Framework 4.5
**Recommended**: Windows 10 / 11 64-bit, 2 GHz dual-core, 1 GB RAM, .NET 6.0+

---

## Comparison vs Other Free Auto Clickers

| | OP Auto Clicker | GS Auto Clicker | AutoHotkey |
|--|:--:|:--:|:--:|
| Max CPS | **100+** | 50 | 1000+ (scripted) |
| Min interval | **1 ms** | 10 ms | 1 ms |
| Open source | ✅ | ❌ | ✅ |
| Portable (no installer) | ✅ | ❌ | ❌ |
| File size | **512 KB** | 5 MB | 4 MB |
| Bundleware in installer | None | Historically yes | None |
| Easy for beginners | ✅ | ✅ | ❌ (scripting language) |

Full comparison: [opauto.app/op-auto-clicker-vs-gs-auto-clicker](https://opauto.app/op-auto-clicker-vs-gs-auto-clicker)
All alternatives compared: [opauto.app/op-auto-clicker-alternatives](https://opauto.app/op-auto-clicker-alternatives)

---

## FAQ

**Is OP Auto Clicker really free?**
Yes. Free for personal and commercial use. No premium tier, no subscriptions, no ads. Open source under the [MIT License](LICENSE).

**Will I get banned for using OP Auto Clicker in games?**
Single-player and most casual servers permit auto-clicking. Major competitive servers (Hypixel, Mineplex) and games with advanced anti-cheats (Vanguard, Easy Anti-Cheat) prohibit any automation. Always check each game's terms before using competitively.

**Why does my antivirus flag OP Auto Clicker?**
AV engines flag any program that sends synthetic mouse input — a behavior shared with malware. Submit the file to [VirusTotal](https://www.virustotal.com): it shows clean across major engines. Add an exception in your AV if needed.

**Does OP Auto Clicker work on Windows 11?**
Yes — fully tested on Windows 11 (32-bit, 64-bit, builds 23H2 and 24H2).

**Why does Windows SmartScreen warn me?**
SmartScreen warns about any executable that hasn't built up a "reputation" through millions of installs via the Microsoft Store. Click "More info" then "Run anyway".

20 more answers: [opauto.app/faq](https://opauto.app/faq)

---

## Contributing

PRs welcome. Please open an issue first to discuss any major changes.

```bash
git clone https://github.com/op-auto-clicker/op-auto-clicker.git
cd op-auto-clicker
# Build instructions in BUILDING.md
```

---

## License

MIT License — see [LICENSE](LICENSE) for details. Free for personal and commercial use.

---

## Links

- **Website**: [opauto.app](https://opauto.app)
- **Download**: [opauto.app/download](https://opauto.app/download)
- **Documentation**: [opauto.app/how-to-use-auto-clicker](https://opauto.app/how-to-use-auto-clicker)
- **FAQ**: [opauto.app/faq](https://opauto.app/faq)
- **About the project**: [opauto.app/about](https://opauto.app/about)

---

**Topics**: `auto-clicker` `windows` `automation` `clicker` `gaming` `minecraft` `roblox` `accessibility` `cps` `open-source` `csharp` `dotnet`
