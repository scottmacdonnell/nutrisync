//
//  SettingsView.swift
//  Nutrisync
//
//  Created by Scott MacDonnell on 2024-03-20.
//

import SwiftUI

struct SettingsView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading) {
                HStack {
                    Text("Settings")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                    
                    Spacer()
                }
            }
            .padding()
        }
    }
}

#Preview {
    SettingsView()
}
