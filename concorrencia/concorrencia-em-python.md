# ⚡ Roadmap – Concorrência e Paralelismo em Python

> Guia modular para aprender concorrência, paralelismo e assincronismo em Python.  
> Use os checkboxes `[ ]` para acompanhar seu progresso.

---

## 1. Fundamentos
- [ ] Diferença entre concorrência, paralelismo e assincronismo
- [ ] Processos vs Threads
- [ ] O que é GIL (Global Interpreter Lock)

## 2. Threads em Python
- [ ] threading.Thread
- [ ] Lock, RLock, Condition, Semaphore
- [ ] Queue para comunicação segura entre threads
- [ ] Exemplo: downloader com múltiplas threads

## 3. Multiprocessing
- [ ] multiprocessing.Process
- [ ] Pool de processos
- [ ] Pipe e Queue
- [ ] Shared memory
- [ ] Exemplo: cálculo pesado em paralelo

## 4. Futures e Executors
- [ ] concurrent.futures.ThreadPoolExecutor
- [ ] concurrent.futures.ProcessPoolExecutor
- [ ] Submeter e coletar resultados com futures

## 5. Asyncio
- [ ] async/await – corrotinas
- [ ] asyncio.run, gather, create_task
- [ ] asyncio.Queue
- [ ] Exemplo: cliente HTTP assíncrono

## 6. Integração com IO Assíncrono
- [ ] aiohttp para chamadas HTTP
- [ ] databases assíncronas (asyncpg, motor para MongoDB)
- [ ] WebSockets assíncronos (websockets, FastAPI)

## 7. Sincronização e Coordenação
- [ ] Locks em multiprocessing
- [ ] Eventos e barriers
- [ ] Timeouts e cancelamento de tarefas

## 8. Padrões de Concorrência
- [ ] Map-Reduce
- [ ] Produtor-Consumidor
- [ ] Fan-in / Fan-out
- [ ] Actor model (padrão Erlang adaptado)

## 9. Ferramentas e Boas Práticas
- [ ] Profiling de concorrência (timeit, perf)
- [ ] Evitar deadlocks e race conditions
- [ ] Uso de bibliotecas de alto nível (Trio, AnyIO)
- [ ] Quando não usar concorrência (código bound a CPU com GIL)
