# ~/.bashrc — Asish's custom Bash config
# =====================================

# Exit if not interactive (prevents errors in non-login shells)
[[ $- != *i* ]] && return

# ─────────────────────────────
# 🧠 Environment and colors
# ─────────────────────────────
export TERM=xterm-256color
export EDITOR=nvim
export VISUAL=nvim
export PATH="$HOME/.local/bin:$PATH"

# ─────────────────────────────
# 🎨 Aliases for convenience
# ─────────────────────────────
alias ls='eza --icons=always --color=auto'
alias ll='eza -lah --icons=always --color=auto'
alias la='eza -a --icons=always --color=auto'
alias l='eza -1 --icons=always --color=auto'
alias tree='tree -C'
alias grep='grep --color=auto'
alias cls='clear'
alias vi='nvim'
alias vim='nvim'
alias wlogin='python /home/asish0604/Scripts/Captive-Login/wifi-login.py'

# ─────────────────────────────
# ⚙️ History setup
# ─────────────────────────────
HISTCONTROL=ignoredups:erasedups
HISTSIZE=10000
HISTFILESIZE=20000
shopt -s histappend

# ─────────────────────────────
# ⚡ Prompt / Oh My Posh
# ─────────────────────────────
if command -v oh-my-posh >/dev/null 2>&1; then
  eval "$(oh-my-posh init bash --config ~/.poshthemes/jandedobbeleer.omp.json)"
else
  # Fallback prompt if oh-my-posh isn't installed
  PS1="\[\e[1;32m\]\u@\h \[\e[1;34m\]\w \$\[\e[0m\] "
fi

# ─────────────────────────────
# 🧰 Quality-of-life shell options
# ─────────────────────────────
# Make tab completion smarter
bind 'set completion-ignore-case on'
bind 'set show-all-if-ambiguous on'

# Less clutter in Python REPL and pip
export PYTHONPYCACHEPREFIX="$HOME/.cache/pycache"

# ─────────────────────────────
# 🧠 Custom greeting (optional)
# ─────────────────────────────
echo -e "\e[1;35mWelcome back, Asish 👋 — stay focused and build cool things.\e[0m"
