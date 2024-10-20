{
    "targets": [
        {
            "target_name": "node-imgui",
            "cflags!": [ "-fno-exceptions" ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "sources": [
                "./hello.cc",
                "./deps/imgui/imgui.cpp",
                "./deps/imgui/imgui_draw.cpp",
                "./deps/imgui/imgui_widgets.cpp",
                "./deps/imgui/imgui_tables.cpp",
                "./deps/imgui/backends/imgui_impl_glfw.cpp",
                "./deps/imgui/backends/imgui_impl_opengl3.cpp"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "./deps/imgui",
                "./deps/imgui/backends",
                "./deps/glfw/include"
            ],
            'cflags_cc': ['-std=c++23', '-fno-exceptions'],
            'cflags': ['-fno-exceptions'],
            'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
            'conditions': [
                ['OS=="win"', {
                    'libraries': ['../glfw3dll.lib', '../opengl32.lib'],
                    'defines': ['WIN32_LEAN_AND_MEAN', 'VC_EXTRALEAN', '_WIN32', '_HAS_EXCEPTIONS=0'],
                    'msvs_settings' : {
                        'VCCLCompilerTool' : {
                            'AdditionalOptions' : [
                                '/O2','/Oy','/GL','/GF','/Gm-', '/std:c++23',
                                '/EHa-s-c-','/MT','/GS','/Gy','/GR-','/Gd',
                            ]
                        },
                        'VCLinkerTool' : {
                            'AdditionalOptions' : ['/DEBUG:NONE', '/LTCG', '/OPT:NOREF'],
                        },
                    },
                }],
            ],
        }
    ]
}