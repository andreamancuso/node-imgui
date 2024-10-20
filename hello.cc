#include <napi.h>

static Napi::Value Test(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();

  return env.Null();
}

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports["Test"] = Napi::Function::New(env, Test);

  return exports;
}

NODE_API_MODULE(hello, Init)
