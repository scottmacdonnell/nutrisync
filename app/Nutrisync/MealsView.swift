//
//  MealsView.swift
//  Nutrisync
//
//  Created by Scott MacDonnell on 2024-03-20.
//

import SwiftUI

struct MealsView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading) {
                HStack {
                    Text("Meals")
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
    MealsView()
}
