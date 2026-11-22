FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# uv, pinned so everyone gets the same version.
COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /uvx /usr/local/bin/

ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never
